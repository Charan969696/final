from app import app, db, FoodItem

def populate_food_items():
    food_items = [
        # Diabetes-friendly Telugu foods
        {
            'name': 'Ragi Dosa with Mint Chutney',
            'description': 'Thin crepes made from finger millet flour, served with fresh mint chutney',
            'price': '120',
            'health_benefits': 'Low glycemic index, high fiber, rich in calcium',
            'suitable_for': 'diabetes',
            'image_url': '/static/images/food/ragi dosa mint chutney.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Bajra Upma with Vegetables',
            'description': 'Pearl millet cooked with mixed vegetables and mild spices',
            'price': '100',
            'health_benefits': 'Low glycemic, high protein, rich in fiber',
            'suitable_for': 'diabetes',
            'image_url': '/static/images/food/bajra upma with vegetables.jpg ',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Korra Annam with Dal',
            'description': 'Foxtail millet rice with protein-rich dal and vegetables',
            'price': '150',
            'health_benefits': 'Low glycemic, high protein, rich in fiber',
            'suitable_for': 'diabetes',
            'image_url': '/static/images/food/korra annam with dal.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Jonna Roti with Palakura Pappu',
            'description': 'Sorghum flatbread with spinach dal',
            'price': '130',
            'health_benefits': 'Low glycemic, high protein, rich in iron',
            'suitable_for': 'diabetes',
            'image_url': '/static/images/food/jonna rotti with palakura pappu.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Grilled Fish with Brown Rice',
            'description': 'Grilled fish marinated in Telugu spices, served with brown rice and vegetables',
            'price': '180',
            'health_benefits': 'Rich in omega-3, low carb, high protein',
            'suitable_for': 'diabetes',
            'image_url': '/static/images/food/grilled fish with brown rice.jpg',
            'meal_type': 'dinner'
        },
        {
            'name': 'Korra Khichdi',
            'description': 'Foxtail millet cooked with moong dal and vegetables',
            'price': '130',
            'health_benefits': 'Low glycemic, high protein, rich in fiber',
            'suitable_for': 'diabetes',
            'image_url': '/static/images/food/korra khichidi.jpg',
            'meal_type': 'dinner'
        },

        # Heart Disease-friendly Telugu foods
        {
            'name': 'Oats Upma with Vegetables',
            'description': 'Steel-cut oats cooked with mixed vegetables and mild spices',
            'price': '100',
            'health_benefits': 'Healthy fats, high fiber, low cholesterol',
            'suitable_for': 'heart_disease',
            'image_url': '/static/images/food/oatss upma with vegetables.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Ragi Malt with Nuts',
            'description': 'Finger millet porridge with almonds and walnuts',
            'price': '90',
            'health_benefits': 'Heart-healthy fats, rich in antioxidants',
            'suitable_for': 'heart_disease',
            'image_url': '/static/images/food/ragi malt fruits.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Bajra Roti with Gongura Dal',
            'description': 'Pearl millet flatbread with sorrel leaves dal',
            'price': '140',
            'health_benefits': 'Heart-healthy fats, rich in antioxidants',
            'suitable_for': 'heart_disease',
            'image_url': '/static/images/food/bajra roti with gongura dal.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Quinoa Pongal',
            'description': 'Quinoa cooked with moong dal and mild spices',
            'price': '150',
            'health_benefits': 'Heart-healthy, high protein, rich in fiber',
            'suitable_for': 'heart_disease',
            'image_url': '/static/images/food/quinoa pongal.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Grilled Chicken with Brown Rice',
            'description': 'Grilled chicken marinated in Telugu spices, served with brown rice',
            'price': '160',
            'health_benefits': 'Low fat, high protein, rich in minerals',
            'suitable_for': 'heart_disease',
            'image_url': '/static/images/food/grilled chicken with brown rice.jpg',
            'meal_type': 'dinner'
        },
        {
            'name': 'Fish Curry with Brown Rice',
            'description': 'Fish cooked in tomato-based curry with brown rice',
            'price': '160',
            'health_benefits': 'Low fat, high omega-3, rich in minerals',
            'suitable_for': 'heart_disease',
            'image_url': '/static/images/food/fish curry with brown rice.jpg',
            'meal_type': 'dinner'
        },

        # Hypertension-friendly Telugu foods
        {
            'name': 'Ragi Malt with Fruits',
            'description': 'Finger millet porridge with seasonal fruits',
            'price': '90',
            'health_benefits': 'Low sodium, high potassium, rich in calcium',
            'suitable_for': 'hypertension',
            'image_url': '/static/images/food/ragi malt fruits.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Bajra Upma with Vegetables',
            'description': 'Pearl millet cooked with mixed vegetables and mild spices',
            'price': '110',
            'health_benefits': 'Low sodium, high potassium, rich in fiber',
            'suitable_for': 'hypertension',
            'image_url': '/static/images/food/bajra upma with vegetables.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Korra Annam with Sambar',
            'description': 'Foxtail millet rice with mixed vegetable sambar',
            'price': '130',
            'health_benefits': 'Low sodium, high potassium, plant-based protein',
            'suitable_for': 'hypertension',
            'image_url': '/static/images/food/korra annam with sambar.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Jonna Roti with Dal',
            'description': 'Sorghum flatbread with protein-rich dal',
            'price': '150',
            'health_benefits': 'Low sodium, high potassium, rich in fiber',
            'suitable_for': 'hypertension',
            'image_url': '/static/images/food/jonna roti with dal.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Grilled Fish with Vegetables',
            'description': 'Grilled fish with Telugu spices, served with steamed vegetables',
            'price': '170',
            'health_benefits': 'Low sodium, high potassium, lean protein',
            'suitable_for': 'hypertension',
            'image_url': '/static/images/food/grilled fish with vegetables.jpg',
            'meal_type': 'dinner'
        },
        {
            'name': 'Korra Khichdi',
            'description': 'Foxtail millet cooked with moong dal and vegetables',
            'price': '130',
            'health_benefits': 'Low sodium, high potassium, rich in fiber',
            'suitable_for': 'hypertension',
            'image_url': '/static/images/food/korra khichidi.jpg',
            'meal_type': 'dinner'
        },

        # Celiac-friendly Telugu foods
        {
            'name': 'Ragi Dosa with Coconut Chutney',
            'description': 'Gluten-free crepes made from finger millet, served with coconut chutney',
            'price': '110',
            'health_benefits': 'Gluten-free, high protein, rich in calcium',
            'suitable_for': 'celiac',
            'image_url': '/static/images/food/ragi dosa with coconut chutney.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Bajra Upma with Vegetables',
            'description': 'Pearl millet cooked with mixed vegetables and mild spices',
            'price': '100',
            'health_benefits': 'Gluten-free, high protein, rich in fiber',
            'suitable_for': 'celiac',
            'image_url': '/static/images/food/bajra upma with vegetables.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Korra Annam with Dal',
            'description': 'Foxtail millet rice with protein-rich dal',
            'price': '140',
            'health_benefits': 'Gluten-free, balanced nutrients',
            'suitable_for': 'celiac',
            'image_url': '/static/images/food/korra annam with dal.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Jonna Roti with Dal',
            'description': 'Sorghum flatbread with protein-rich dal',
            'price': '150',
            'health_benefits': 'Gluten-free, high protein, rich in minerals',
            'suitable_for': 'celiac',
            'image_url': '/static/images/food/jonna roti with dal.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Grilled Fish with Brown Rice',
            'description': 'Grilled fish with Telugu spices, served with brown rice',
            'price': '160',
            'health_benefits': 'Gluten-free, high protein, omega-3 fatty acids',
            'suitable_for': 'celiac',
            'image_url': '/static/images/food/grilled fish with brown rice.jpg',
            'meal_type': 'dinner'
        },
        {
            'name': 'Korra Khichdi',
            'description': 'Foxtail millet cooked with moong dal and vegetables',
            'price': '130',
            'health_benefits': 'Gluten-free, high protein, rich in fiber',
            'suitable_for': 'celiac',
            'image_url': '/static/images/food/korra khichidi.jpg',
            'meal_type': 'dinner'
        },

        # Obesity-friendly Telugu foods
        {
            'name': 'Ragi Malt with Nuts',
            'description': 'Finger millet porridge with almonds and walnuts',
            'price': '100',
            'health_benefits': 'High protein, low calorie, rich in fiber',
            'suitable_for': 'obesity',
            'image_url': '/static/images/food/ragi malt fruits.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Bajra Upma with Vegetables',
            'description': 'Pearl millet cooked with mixed vegetables and mild spices',
            'price': '90',
            'health_benefits': 'Low calorie, high fiber, rich in nutrients',
            'suitable_for': 'obesity',
            'image_url': '/static/images/food/bajra upma with vegetables.jpg',
            'meal_type': 'breakfast'
        },
        {
            'name': 'Korra Annam with Sambar',
            'description': 'Foxtail millet rice with mixed vegetable sambar',
            'price': '130',
            'health_benefits': 'Low calorie, high protein, rich in fiber',
            'suitable_for': 'obesity',
            'image_url': '/static/images/food/korra annam with sambar.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Jonna Roti with Dal',
            'description': 'Sorghum flatbread with protein-rich dal',
            'price': '150',
            'health_benefits': 'Low calorie, high protein, rich in fiber',
            'suitable_for': 'obesity',
            'image_url': '/static/images/food/jonna roti with dal.jpg',
            'meal_type': 'lunch'
        },
        {
            'name': 'Grilled Fish with Vegetables',
            'description': 'Grilled fish with Telugu spices, served with steamed vegetables',
            'price': '160',
            'health_benefits': 'Low calorie, high protein, omega-3 fatty acids',
            'suitable_for': 'obesity',
            'image_url': '/static/images/food/grilled fish with vegetables.jpg',
            'meal_type': 'dinner'
        },
        {
            'name': 'Grilled Chicken with Brown Rice',
            'description': 'Grilled chicken marinated in Telugu spices, served with brown rice',
            'price': '160',
            'health_benefits': 'Low calorie, high protein, rich in minerals',
            'suitable_for': 'obesity',
            'image_url': '/static/images/food/grilled chicken with brown rice.jpg',
            'meal_type': 'dinner'
        }
    ]

    with app.app_context():
        try:
            # Clear existing food items
            FoodItem.query.delete()
            
            # Add new food items
            for item in food_items:
                food = FoodItem(**item)
                db.session.add(food)
            
            db.session.commit()
            print("Database populated with food items successfully!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            db.session.rollback()

if __name__ == '__main__':
    populate_food_items() 